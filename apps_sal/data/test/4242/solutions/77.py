A,B,K = map(int,input().split())
# print(A,B,K)
A_list = []
ans_list = []

for i in range(1,A+1):
    if A % i == 0 :
        A_list.append(i)
# print(A_list)

for n in A_list:
    if B % n == 0 :
        ans_list.append(n)
# print(ans_list)
print(ans_list[-K])
