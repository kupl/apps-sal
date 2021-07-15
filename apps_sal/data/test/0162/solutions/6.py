def main():
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	arr = [i for i in arr if k % i == 0]
	print(k // max(arr))

main()
