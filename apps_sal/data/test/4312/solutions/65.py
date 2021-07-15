import sys

a, b, c, d = map(int,input().split())

for _ in range(100):
    a_t = c-b
    if a_t <= 0:
        print('Yes')
        return
    c = a_t
    
    t_t = a-d
    if t_t <= 0:
        print('No')
        return

    a = t_t
