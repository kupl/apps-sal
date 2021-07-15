#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))
  
n,q=input2()
B=str(input())
LR=[input_array() for _ in range(q)]

# E=["A","C","G","T"]
T=[0]*(n+1) #1文字目〜n文字目までに出現する"AC"数の累積和

for i in range(n):
	if B[i:i+2] == "AC":	
		T[i+1] = T[i]+1
	else:
		T[i+1]=T[i]
for lr in LR:
	st=lr[0]-1
	fi=lr[1]-1
	print(T[fi]-T[st])
