n, k = map(int, input().split())
s = input()
for i in range(len(s)):
    if(i == k - 1):
        print(str.lower(s[i]), end='')
    else:
        print(s[i], end='')
print()
