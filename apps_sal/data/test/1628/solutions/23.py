import math
import sys
3


def change_char_at(ch, s, indx):
    """
    Strings in Python are immutable objects. So, it is not possible to change a
    certain character in a string in place. For example, an attempt to run the
    following code will fail with a TypeError:

        s = "spam"
        s[1] = "z" # TypeError: 'str' object does not support item assignment

    What this function does is it provides you with a nice interface when you
    want to change a character in a string at a certain index position. So, use
    this function instead of doing everything manually which can sometimes be
    tricky. Notice that the character parameter does not necessarily have to be
    one character long. It can be an empty string which means that a character
    at a certain position will effectively be deleted from the string. If it's
    more than one character long, then they all will be inserted into the string
    starting at the specified index position.

    Parameters:
    ch:   character to insert
    s:    string to insert into
    indx: index position where to insert the character
    """
    if type(ch) is not str:
        raise TypeError('first argument must be a string')
    if type(s) is not str or not len(s) > 0:
        raise TypeError('second argument must be a non-empty string')
    length = len(s) - 1
    if not (indx >= 0 and indx <= length):
        msg = 'string index out of range; '
        msg += 'attempt to access index at {0}; '.format(indx)
        msg += 'allowable index range 0 to {0}'.format(length)
        raise IndexError(msg)
    return s[:indx] + ch + s[indx + 1:]
    "\n    Another possible implementation:\n\n        ls       = list(s)\n        ls[indx] = ch\n        return ''.join(ls)\n\n    This works well too and is equally good, but might be conspired unpythonic\n    by some compared to the one right above it.\n    "


s = input()
x = 0
y = 0
for i in range(0, len(s)):
    if s[i] == 'y':
        y += 1
    elif s[i] == 'x':
        x += 1
if x - y > 0:
    print('x' * (x - y))
else:
    print('y' * (y - x))
