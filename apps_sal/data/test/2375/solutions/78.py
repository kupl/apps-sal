# solution
import io

nim,mike = map(int,input().split())
print("Brown" if abs(nim-mike)<2 else "Alice")
