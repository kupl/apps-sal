n = int(input())
(soft, hard) = (0, 0)
for i in range(n):
    (sir, tip) = input().split()
    if tip == 'soft':
        soft += 1
    else:
        hard += 1
for k in range(100):
    a = k * k // 2
    b = k * k - a
    if soft <= a and hard <= b or (soft <= b and hard <= a):
        print(k)
        break
