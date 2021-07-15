def main():
	h, n = list(map(int, input().split()))
	l = [int(v) for v in input().split()]
	total = sum(l)
	if total>= h:
		return "Yes"
	return "No"	

def __starting_point():
    print((main()))

__starting_point()
