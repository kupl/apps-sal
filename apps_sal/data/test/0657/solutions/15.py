import sys

def main():
    yellow_crystals, blue_crystals = list(map(int, input().split()))
    yellow, green, blue = list(map(int, input().split()))
    
    yellow_req = yellow * 2 + green
    blue_req = green + blue * 3
    
    print(max(0, yellow_req - yellow_crystals) + max(0, blue_req - blue_crystals))
    
	
def __starting_point():
    main() 
    

__starting_point()
