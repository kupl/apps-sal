
def main():
	n, r = list(map(int, input().split()))
	if n>= 10:
		return r
	else:
		return r + (100 * (10 -n))
	

def __starting_point():
    print((main()))

__starting_point()
