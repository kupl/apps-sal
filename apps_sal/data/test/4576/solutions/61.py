A = int(input())  # 500円玉
B = int(input())  # 100円玉
C = int(input())  # 50円玉
X = int(input())  # 合計金額。50の倍数
count = 0

for a in range(0, A + 1):
    for b in range(0, B + 1):
        for c in range(0, C + 1):
            if 500 * a + 100 * b + 50 * c == X:
                count = count + 1
print(count)
