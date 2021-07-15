n = input()

src = list(int(x) for x in input().split())
cp = src.copy()

cp.sort()

def search(arr, val, border):
	for x in range(border, len(arr)):
		if arr[x] == val:
			return x
	print("ERROR!")

pairs = list()
def main():
	for index, val in enumerate(cp):
		tmp = src[index]
		if val != tmp:
			swap = search(src, val, index)
			pairs.append((index, swap))
			src[index] = src[swap]
			src[swap] = tmp
	
	print(len(pairs))
	for x, y in pairs:
		print(x,y)
		
	
main()
