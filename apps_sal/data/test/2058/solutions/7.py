(a, b) = (input(), input())
(alen, blen) = (len(a), len(b))
diff = blen - alen
count = b[:diff + 1].count('0')
result = 0
for i in range(0, alen):
    result += diff + 1 - count if a[i] == '0' else count
    if i == alen - 1:
        break
    count -= 1 if b[i] == '0' else 0
    count += 1 if b[diff + 1 + i] == '0' else 0
print(result)
