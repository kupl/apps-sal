import collections

n = int(input())
a = list(map(int, input().split()))
cnt = collections.Counter(a)
mod = 7 + 10**9
if n % 2 == 0:
    for i in range(1, 1 + n // 2):
        if (i * 2 - 1) not in cnt.keys() or cnt[i * 2 - 1] != 2:
            print(0)
            return

else:
    if 0 not in cnt.keys() or cnt[0] != 1:
        print(0)
        return
    for i in range(1, 1 + n // 2):
        if i * 2 not in cnt.keys() or cnt[i * 2] != 2:
            print(0)
            return
print(2 ** (n // 2) % mod)
