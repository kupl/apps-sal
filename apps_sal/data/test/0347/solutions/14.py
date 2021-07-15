times = list(map(int, input().split()))
att = list(map(int, input().split()))
n,m = list(map(int, input().split()))
sc = 0
for i in range(5):
	sc += max ( 150 * (i+1),  ( 1 - times[i] / 250 ) * 500 * (i+1) - 50 * att[i] )
sc += 100 * n 
sc -= 50 * m
print(int(sc)) 


