aris_card , bob_card = map(int, input(). split())

if aris_card == 1:
    aris_card += 13
if bob_card == 1:
    bob_card += 13

if aris_card == bob_card:
    print( "Draw" )
elif aris_card > bob_card:
    print( "Alice" )
elif aris_card < bob_card:
    print( "Bob" )
