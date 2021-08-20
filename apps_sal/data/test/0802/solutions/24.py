n = int(input())
stri = input()
dict = {}
lenght = len(set(stri))
count = 0
j = 0
result = 999999999
for i in range(n):
    if stri[i] not in dict:
        dict[stri[i]] = 0
        count += 1
    dict[stri[i]] += 1
    if count == lenght:
        while dict[stri[j]] > 1:
            dict[stri[j]] -= 1
            j += 1
        result = min(result, i - j + 1)
print(result)
