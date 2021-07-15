import sys
import heapq

def main():
	N = int(input())
	a = list(map(int, input().split()))

	left = a[0 : N]
	right = a[N*2 : N*3]

	for i in range(N):
		right[i] *= -1

	left_sum = 0
	right_sum = 0

	heap_left = []
	heap_right = []

	for i in range(N):
		left_sum += left[i]
		heapq.heappush(heap_left, left[i])
		right_sum += right[i]
		heapq.heappush(heap_right, right[i])

	temp1 = [0] * (N + 1)
	temp2 = [0] * (N + 1)

	temp1[0] = left_sum
	temp2[N] = right_sum

	for i in range(0, N):
		left_sum += a[N+i]
		heapq.heappush(heap_left, a[N+i])
		left_sum -= heapq.heappop(heap_left)
		temp1[i+1] = left_sum

	for i in range(0, N):
		right_sum -= a[N*2-1-i]
		heapq.heappush(heap_right, -a[N*2-1-i])
		right_sum -= heapq.heappop(heap_right)
		temp2[N - 1 - i] = right_sum

	ans = -100000000000000000000000000000000000000000
	for i in range(0, N + 1):
		x = temp1[i] + temp2[i]
		if(ans < x):
			ans = x
	print(ans)
main()
