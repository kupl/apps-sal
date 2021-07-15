n = int(input())
s = input()
all_types = set()
count = {}
for c in s:
    all_types.add(c)
    count[c] = 0
n_all_types = len(all_types)
def solve():
    ret = n
    first = 0
    last = 0
    n_types = 0
    while first <= last:
        while n_types < n_all_types:
            if last == n:
                return ret
            if count[s[last]] == 0:
                n_types += 1
            count[s[last]] += 1
            last += 1
        ret = min(ret, last - first)
        if count[s[first]] == 1:
            n_types -= 1
        count[s[first]] -= 1
        first += 1
    return ret
print(solve())

