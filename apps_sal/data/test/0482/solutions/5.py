
password = ''
n, k = list(map(int, input().split()))
alph = [chr(i) for i in range(97, 97 + k)]

for i in range(n):
    password += alph[i % k]

print(password)
