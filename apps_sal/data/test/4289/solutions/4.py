N = int(input())

T, A = [int(i) for i in input().split()]

h_list = list(map(int, input().split()))

temp_list = [(i, abs(A - (T-x*0.006))) for i, x in enumerate(h_list, 1)]

ans = min(temp_list, key=lambda x: x[1])

print((ans[0]))

