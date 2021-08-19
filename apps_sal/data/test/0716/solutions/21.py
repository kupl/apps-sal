n, a, b = list(map(int, input().split()))
s = input()

a -= 1
b -= 1
if s[a] == s[b]:
    print(0)
else:
    print(1)
    #i = a
    # while s[i] != s[b]:
    #i += 1
   # j = a
    # while j > 0 and s[i] != s[b]:
    #j -= a
