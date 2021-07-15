N = int(input())
s = list(input().split())

def answer(N:int, s: str) -> str:
    if 'Y' in s:
	    return 'Four'
    else:
	    return 'Three'
    
    
print(answer(N, s))
