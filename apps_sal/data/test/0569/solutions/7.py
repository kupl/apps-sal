n = int(input())
if (n > 26):
    print(-1)
else:
    s = input().rstrip()
    print(len(s) - len(set(list(s))))
