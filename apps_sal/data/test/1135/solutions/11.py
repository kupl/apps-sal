n = int(input())
s = input().rstrip()
s1 = s[-1 - n % 2::-2] + s[::2]
print(s1 if n % 2 else s1[::-1])
