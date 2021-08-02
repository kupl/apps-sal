n = int(input())
ret = ""
alphabet = list("abcdefghijklmnopqrstuvwxyz")
while n:
    n -= 1
    n, mod = divmod(n, 26)
    ret += alphabet[mod]
print(ret[::-1])
