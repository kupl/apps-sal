h1, m1 = list(map(int, input().split(':')))
h2, m2 = list(map(int, input().split(':')))
q1 = h1*60+m1
q2 = h2*60+m2
q3 = (q1+q2)/2
h3 = int(q3 // 60)
m3 = int(q3 % 60)
print("{:02d}:{:02d}".format(h3,m3))

