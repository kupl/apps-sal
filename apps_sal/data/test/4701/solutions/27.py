n=int(input())
k=int(input())
given_integer=1
#Option A:-To Increase The Value By double
#Option B:-To Increase Value By K

for i in range(0,n):
	given_integer=min(given_integer*2,given_integer+k)

print((int(given_integer)))

