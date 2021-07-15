a,b=map(int, input().split())
print("Alice" if (a+12)%14>(b+12)%14 else "Draw" if a==b else "Bob")
