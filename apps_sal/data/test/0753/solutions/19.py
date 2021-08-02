from fractions import gcd


def Irreducible_Fraction(A, B):
    ''' Returns list of two integers representing the nominator and denominator of the Irreducible version of A/B '''
    x = gcd(A, B)
    return [A // x, B // x]


a, b, c, d = map(int, input().split())

# Movie Frame Ratio:
F = a / b

# Screen Ratio:
S = c / d


# There are three case:
(a / b < c / d)
(a / b == c / d)
(a / b > c / d)


# Case 1:
# Frame's ratio is larger than screen ratio (c/d > a/b)
# This means that if both the screen and the movie had the same vertical length,
# The movie's horizontal length will be bigger which is not desired !
# So in this case, we will stretch the movie until it is the same horizontal length as the screen,( c -> a )
# And the movie's vertical length would be smaller than the screen's vertical length.( d < b )
# Stretching factor = a/c
if(a / b < c / d):
    stretching_factor = a / c
    # To avoid decimals which may result into an error while computing the fraction
    # We will multiply both the the new area and te screen area by c
    New_horizontal = a
    New_vertical = a * d  # The multiplied c apears in ommiting the division by c in the stretching factor
    New_Movie_Area = int(New_horizontal * New_vertical)
    Screen_Area = int(a * b * c)  # The multiplied c appears
    Empty_Area = Screen_Area - New_Movie_Area
    desired_ratio = Irreducible_Fraction(Empty_Area, Screen_Area)
    nominator = desired_ratio[0]
    denominator = desired_ratio[1]
    print(nominator, end="/")
    print(denominator)


# Case 2:
# Frame's ratio is the same as the screen ratio (c/d == a/b)
# This means that we can stretch the movie till it is the same horizontal length as the screen,
# And the vertical length of the movie would be the same as the vertical length of the screen
# So The empty area will always be ZERO !


elif(a / b == c / d):
    print("0/1")


# Case 3:
# Opposite to Case 1
# Frame's ratio is smaller than screen ratio (c/d > a/b)
# This means that the stretching process will end when the vertical length is the same for the screen and the frame
# While the horizontal length of the screen is bigger
# Stretching facto = b/d
else:
    stretching_factor = b / d
    # To_avoid decimals, the same as case 1 was done !
    New_vertical = b
    New_horizontal = (b) * c
    New_Movie_Area = int(New_horizontal * New_vertical)
    Screen_Area = int(a * b * d)
    Empty_Area = Screen_Area - New_Movie_Area
    desired_ratio = Irreducible_Fraction(Empty_Area, Screen_Area)
    nominator = desired_ratio[0]
    denominator = desired_ratio[1]
    print(nominator, end="/")
    print(denominator)
