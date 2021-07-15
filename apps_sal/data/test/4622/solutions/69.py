def main():
	n = int(input())
	l = [int(v) for v in input().split()]
	if len(set(l)) == n:
		return "YES"
	return "NO"
	

def __starting_point():
    print((main()))

__starting_point()
