import sys
n = input()
li = list(map(int, input().split()))

# 黒板にかかれている文字は全部偶数か？
for i in li:
    if i % 2 != 0:
        print("0")
        return

# 黒板にかかれている文字を全部2で割っていく
count = 0

while(True):
    for index, item in enumerate(li):
        if item % 2 == 0:
            li[index] = item / 2
        else:
            print(count)
            return
    count += 1
