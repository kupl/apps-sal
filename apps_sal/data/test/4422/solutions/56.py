n,k = map(int, input().split())
s = input()
k -= 1
print(s[:k] + s[k].lower() + s[k+1:])
