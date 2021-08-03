class heap:
    def __init__(self, maxn):
        self.a = [0] * maxn
        self.size = 0

    def shift_down(self, i):
        while 2 * i + 1 < self.size:
            l = 2 * i + 1
            r = 2 * i + 2
            j = l
            if r < self.size and self.a[r] < self.a[l]:
                j = r
            if self.a[i] <= self.a[j]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j

    def shift_up(self, i):
        while i and self.a[i] < self.a[(i - 1) // 2]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    def erase_min(self):
        mn = self.a[0]
        self.a[0] = self.a[self.size - 1]
        self.size -= 1
        self.shift_down(0)
        return mn

    def insert(self, val):
        self.size += 1
        self.a[self.size - 1] = val
        self.shift_up(self.size - 1)


n = int(input())
ans = 0
s = heap(400000 + 100)
for i in [int(j) for j in input().split()]:
    s.insert(i)
if s.size % 2 == 0:
    s.insert(0)
while s.size > 1:
    t = s.erase_min() + s.erase_min()
    if s.size:
        t += s.erase_min()
    ans += t
    s.insert(t)
print(ans)
