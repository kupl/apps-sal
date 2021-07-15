# import math
# N = int(input())
# A_list = [int(i) for i in input().split()]


# def divide_list(num_list):
#   left = 0
#   right = len(num_list)
#   minimum = 10**9

#   while True:
#     c = (left+right)//2
#     left_sum = sum(num_list[:c])
#     right_sum = sum(num_list[c:])
#     diff = abs(left_sum - right_sum)

#     if minimum > diff:
#       minimum = diff
#       minimum_left = left
#       minimum_right = right
    
#     if left_sum > right_sum:
#       right = c
#     elif left_sum < right_sum:
#       left = c
#     else:
#       return num_list[:c], num_list[c:]

#     if c==left or c==right:
#       c = (minimum_left+minimum_right)//2
#       return num_list[:c], num_list[c:]

# tmp1_list, tmp2_list = divide_list(A_list)
# print(tmp1_list, tmp2_list)
# tmp11_list, tmp12_list = divide_list(tmp1_list)
# tmp21_list, tmp22_list = divide_list(tmp2_list)
# print(tmp11_list, tmp12_list, tmp21_list, tmp22_list)

# ans_list = [sum(tmp11_list), sum(tmp12_list), sum(tmp21_list), sum(tmp22_list)]
# ans_list.sort()

# print(ans_list[-1] - ans_list[0])


#102_D
N = int(input())
A = list(map(int, input().split()))
s = 0
AS = []
for i in range(N):
    s += A[i]
    AS.append(s)
#尺取り法
Ans = AS[N-1]+1
L = 0
R = 2
for Mid in range(1, N-2):
    Sum_L = AS[Mid]
    Sum_R = AS[N-1]-Sum_L
    while abs(Sum_L-2*AS[L]) > abs(Sum_L-2*AS[L+1]):
        L += 1

    while abs(AS[N-1]-2*AS[R]+AS[Mid]) > abs(AS[N-1]-2*AS[R+1]+AS[Mid]):
        R += 1
    P = AS[L]
    Q = AS[Mid]-AS[L]
    S = AS[R]-AS[Mid]
    T = AS[N-1]-AS[R]
    #print(Mid,L,R,abs(max(P,Q,S,T)-min(P,Q,S,T)))
    Ans = min(Ans, abs(max(P, Q, S, T)-min(P, Q, S, T)))
print(Ans)

