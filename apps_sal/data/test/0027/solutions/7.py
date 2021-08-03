def R(): return list(map(int, input().split()))


n = int(input())
s = input()

for i in reversed(list(range(n // 2))):
    if s[0:i + 1] == s[i + 1:2 * i + 2]:
        print((n - i))
        return

print(n)
