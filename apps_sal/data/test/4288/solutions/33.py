
def main():
	a, b, c = map(int, input().split())
	if len(set((a,b,c)))==2:
		return "Yes"
	return "No"

def __starting_point():
    print(main())
__starting_point()
