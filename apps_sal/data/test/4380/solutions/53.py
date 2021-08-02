A, B = map(int, input().split())

count = 0  # 初期化
for C in range(1, 4):
    if A * B * C % 2 == 1:
        count = count + 1  # Cに順番に１、２、３と代入していく中で、A×B×C が奇数になるたんびにcountに１加算していく
if count > 0:  # A×B×Cが奇数になるようなCが少なくとも１つ存在していたらYesと表示したい
    print("Yes")

else:
    print("No")
