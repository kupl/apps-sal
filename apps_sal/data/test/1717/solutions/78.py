#n = int(input())
n = 30

# ２で割っても１余るため、Ansは必ず奇数
# multi = 6*10*14*33*26*17*19*23*15*29
multi = 2 * 2 * 4 * 3 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 5 * 29 + 1
print(multi)
# multi = 10 ** 13 - 1
'''
num = 2
while num <= n:
    print(num, ',',multi%num)
    num += 1
'''
