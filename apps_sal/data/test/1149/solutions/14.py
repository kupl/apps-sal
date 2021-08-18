
n = int(input())
p_l = list(map(int, input().split()))
q_l = list(map(int, input().split()))
p = p_l[0]
q = q_l[0]
p_l = p_l[1:]
q_l = q_l[1:]
ll = set(p_l + q_l)
sucess = False

n_sum = (n * (n + 1)) // 2
if n_sum == sum(ll):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
