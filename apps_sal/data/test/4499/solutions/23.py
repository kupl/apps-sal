def answer(a: str, b: str, c: str) -> str:
    return (a[0]+b[0]+c[0])

a,b,c=input().split()
print(answer(a,b,c).upper())
