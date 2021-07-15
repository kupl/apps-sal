n = int(input()) - 1
k = 10 ** n
m = 210 - k % 210
print(k + m if m < 9 * k else -1)
