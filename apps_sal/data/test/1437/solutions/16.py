def count(num):
    string = bin(num)[2:]
    return string.count('0') + 6 - len(string)


key = [3 ** count(x) for x in range(64)]
dic = {}
for i in range(10):
    dic[chr(ord('0') + i)] = key[i]
for i in range(26):
    dic[chr(ord('A') + i)] = key[i + 10]
for i in range(26):
    dic[chr(ord('a') + i)] = key[i + 36]
dic['-'] = key[62]
dic['_'] = key[63]
mod = int(1000000000.0) + 7
string = input()
ans = 1
for x in string:
    ans = ans * dic[x] % mod
print(ans)
