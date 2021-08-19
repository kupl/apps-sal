"""
Catherine has a deck of n cards, each of which is either red, green, or blue.
 As long as there are at least two cards left, she can do one of two actions:

    take any two (not necessarily adjacent) cards with different colors and 
    exchange them for a new card of the third color;
    take any two (not necessarily adjacent) cards with the same color and 
    exchange them for a new card with that color. 

She repeats this process until there is only one card left. What are the 
possible colors for the final card?

Input

The first line of the input contains a single integer n (1\u2009≤\u2009n\u2009≤\u2009200) — 
the total number of cards.

The next line contains a string s of length n — the colors of the cards. 
s contains only the characters 'B', 'G', and 'R', representing blue, green, 
and red, respectively.
Output

Print a single string of up to three characters — the possible colors of 
the final card (using the same symbols as the input) in alphabetical order.
"""
import io
import sys
import time
import random
n = int(input())
cols = 'RGB'
counts = {'R': 0, 'G': 0, 'B': 0}
for c in input():
    counts[c] += 1


def gettwocolors(counts):
    if counts['R'] == 0:
        return 'GB'
    if counts['G'] == 0:
        return 'RB'
    if counts['B'] == 0:
        return 'RG'


def printcols(cols):
    print(sortedcols(cols))


def sortedcols(cols):
    return ''.join(sorted(list(cols)))


complement = {sortedcols('RG'): 'B', sortedcols('RB'): 'G', sortedcols('GB'): 'R'}
if counts['R'] > 0 and counts['G'] > 0 and (counts['B'] > 0):
    printcols('RGB')
else:
    (c1, c2) = gettwocolors(counts)
    if counts[c1] == 0:
        printcols(c2)
    elif counts[c2] == 0:
        printcols(c1)
    elif counts[c1] >= 2 and counts[c2] >= 2:
        printcols('RGB')
    elif counts[c1] >= 2:
        printcols(c2 + complement[sortedcols(c1 + c2)])
    elif counts[c2] >= 2:
        printcols(c1 + complement[sortedcols(c1 + c2)])
    else:
        printcols(complement[sortedcols(c1 + c2)])
