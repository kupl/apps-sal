class bitset():
    def __init__(self, n):
        self.size = 1 << ((n + 2).bit_length())
        self.bit = [0] * (self.size + 1)

    def append(self, val):
        val += 1
        id = val
        while id <= self.size:
            self.bit[id] += 1
            id += (id) & (-id)

    def erase(self, val):
        val += 1
        id = val
        while id <= self.size:
            self.bit[id] -= 1
            id += (id) & (-id)

    def cnt(self, val):
        res_sum = 0
        val += 1
        while val > 0:
            res_sum += self.bit[val]
            val -= val & (-val)
        return res_sum

    def next(self, val):
        val += 1
        base = self.cnt(val - 1)
        start = 0
        end = self.size
        while end - start > 1:
            test = (end + start) // 2
            if self.bit[test] > base:
                end = test
            else:
                start = test
                base -= self.bit[test]
        return end - 1


n = int(input())
s = input()

alice = [int(s[i] == "0") for i in range(n)]
bob = [int(s[i] == "1") for i in range(n)]
for i in range(1, n):
    alice[i] += alice[i - 1]
    bob[i] += bob[i - 1]
alice.append(0)
bob.append(0)

update_que = [[] for i in range(n)]

alice_win = []
id = 0
while id < n:
    if s[id] != "0":
        pos = id
        while pos < n and s[pos] != "0":
            pos += 1
        update_que[pos - id - 1].append(id)
        id = pos
    else:
        id += 1
bob_win = []
id = 0
while id < n:
    if s[id] != "1":
        pos = id
        while pos < n and s[pos] != "1":
            pos += 1
        update_que[pos - id - 1].append(id)
        id = pos
    else:
        id += 1

bst = bitset(n)
bst.append(n)

ans = [0] * n
for i in range(n - 1, -1, -1):
    for id in update_que[i]:
        bst.append(id)
    pos = 0
    res = 0
    while pos < n - i:
        check1 = alice[pos + i] - alice[pos - 1]
        check2 = bob[pos + i] - bob[pos - 1]
        if not check1 or not check2:
            res += 1
            pos += i + 1
        else:
            npos = bst.next(pos)
            if npos == n:
                break
            else:
                pos = npos + i + 1
                res += 1
    ans[i] = res

print(*ans)
