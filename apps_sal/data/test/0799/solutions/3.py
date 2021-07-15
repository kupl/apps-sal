def main():
	n = int(input())
	arr = list(map(int, input().split()))
	x = max(arr)
	print(sum([x - i for i in arr]))


main()
