n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    if a !=b:
        print("rated")
        break
    s.append(b)
else:
    if s[::-1] != sorted(s):
        print("unrated")
    else:
        print("maybe")
