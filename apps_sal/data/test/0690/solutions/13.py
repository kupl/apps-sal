p = {'1': 'O-|O-OOO', '0': 'O-|-OOOO', '3': 'O-|OOO-O', '2': 'O-|OO-OO', '5': '-O|-OOOO', '4': 'O-|OOOO-', '7': '-O|OO-OO', '6': '-O|O-OOO', '9': '-O|OOOO-', '8': '-O|OOO-O'}
print('\n'.join(p[i] for i in input()[:: -1]))
