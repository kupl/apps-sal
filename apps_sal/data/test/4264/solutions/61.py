N = int(input())

# N以下の正の整数のうち、桁数が奇数（1桁、3桁、5桁など）であるようなものの個数を出力

count = 0

for i in range(1, N + 1):
    if (len(str(i))) % 2 == 1:
        count += 1
print(count)
