N = int(input())
T = input()
nums = [1, 1, 0]
ans1 = []
ans2 = []
ans3 = []
for n in range(N):
    ans1.append(str(nums[n % 3]))
for n in range(1, N + 1):
    ans2.append(str(nums[n % 3]))
for n in range(2, N + 2):
    ans3.append(str(nums[n % 3]))
s_ans1 = ''.join(ans1)
s_ans2 = ''.join(ans2)
s_ans3 = ''.join(ans3)
if T == '1':
    print((pow(10, 10) * 2))
elif T == '11':
    print((pow(10, 10)))
elif T == '0':
    print((pow(10, 10)))
elif s_ans1 == T or s_ans2 == T or s_ans3 == T:
    if T[-1] == '0':
        print((pow(10, 10) - T.count('0') + 1))
    else:
        print((pow(10, 10) - T.count('0')))
else:
    print((0))
