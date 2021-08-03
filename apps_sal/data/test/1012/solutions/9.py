n = int(input())
for x in range(n):
    s = input()
    s = ''.join(sorted(list(s)))
    if(s == s[::-1]):
        print(-1)
    else:
        print(s)
