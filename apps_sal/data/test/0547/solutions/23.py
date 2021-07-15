__author__ = 'Think'
def format(ans):
	return ans+5*(ans//k)
n, k=[int(i) for i in input().split()]
freq={i:0 for i in range(1, 105)}
for i in range(n):
	s=input()
	freq[len(s)]+=1
correct=len(input())
t=0
for i in range(1, correct):
	t+=freq[i]
print(format(t)+1, format(t+freq[correct]-1)+1)

