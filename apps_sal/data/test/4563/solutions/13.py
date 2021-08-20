n = int(input())
(t_lst, a_lst) = ([], [])
for i in range(n):
    (ti, ai) = map(int, input().split())
    t_lst.append(ti)
    a_lst.append(ai)
(t, a) = (1, 1)
for i in range(n):
    (ti, ai) = (t_lst[i], a_lst[i])
    n = max((t + ti - 1) // ti, (a + ai - 1) // ai)
    t = n * ti
    a = n * ai
print(t + a)
